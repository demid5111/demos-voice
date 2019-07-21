import {AfterViewInit, Component, ElementRef, OnInit, ViewChild, ViewChildren} from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {Chart} from 'chart.js';

export const chartColors = {
  red: 'rgb(255, 99, 132)',
  orange: 'rgb(255, 159, 64)',
  yellow: 'rgb(255, 205, 86)',
  green: 'rgb(75, 192, 192)',
  blue: 'rgb(54, 162, 235)',
  purple: 'rgb(153, 102, 255)',
  grey: 'rgb(201, 203, 207)'
};


@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements AfterViewInit {
  title = 'ui2';
  configUrl = 'http://localhost:5000';
  allProposals: any[];
  currentProposal: any = null;

  @ViewChild('canvasElement')
  canvasElement: ElementRef;

  @ViewChild('temperatureElement')
  temperatureElement: ElementRef;

  @ViewChild('overallElement')
  overallElement: ElementRef;

  private legend: HTMLElement;
  private tooltip: HTMLElement;
  private answersChart: any;
  private temperatureChart: any;
  private spamChart: any;
  private overallChart: any;
  public url: any;

  constructor(private http: HttpClient) {
    this.allProposals = [];

    this.fetchProposals();
  }

  ngAfterViewInit(): void {
  }

  analyzeProposal() {
    this.http.post(`${this.configUrl}/new`, {fromUrl: this.url, socialNetwork: 'vk'})
      .subscribe((data: any[]) => {
        this.fetchProposals();
      });
  }

  fetchProposals() {
    this.http.get(`${this.configUrl}/all`)
      .subscribe((data: any[]) => {
        this.allProposals = data;

        this.buildOverallChart();
      });
  }

  selectProposal(id) {
    let index = 0;
    this.allProposals.find((el, i) => {
      if (el.id === id) {
        index = i;
        return true;
      }
      return false;
    });

    this.currentProposal = index;
    setTimeout(() => {
      console.log('Waiting for the element');

      this.buildAnswersChart();
      this.buildTemperatureChart();

    }, 200);

  }

  eraseSelection() {
    this.currentProposal = null;

    setTimeout(() => {
      console.log('Waiting for the element');

      this.buildOverallChart();

    }, 200);
  }

  buildAnswersChart() {
    const labels = this.allProposals[this.currentProposal].poll.map((el) => {
      return el.text;
    });

    const rates = this.allProposals[this.currentProposal].poll.map((el) => {
      return el.rate;
    });
    this.answersChart = this.createAnswersChart(
      labels,
      rates,
      [],
    );
  }

  buildOverallChart() {
    const labels = this.allProposals.map((el, i) => {
      return i+1;
    });


    const positives = this.allProposals.map((el) => el.sumPositive);
    const positivesColors = [];
    for (let i=0; i < positives.length; i++) {
      positivesColors.push(chartColors.green);
    }
    const positiveDataset = {
      data: positives,
      labels: 'Позитивно',
      backgroundColor: positivesColors
    };

    const neutrals = this.allProposals.map((el) => el.sumNeutral);
    const neutralsColors = [];
    for (let i=0; i < neutrals.length; i++) {
      neutralsColors.push(chartColors.blue);
    }
    const neutralDataset = {
      data: neutrals,
      labels: 'Нейтрально',
      backgroundColor: neutralsColors
    };

    const negatives = this.allProposals.map((el) => -el.sumNeutral);
    const negativesColors = [];
    for (let i=0; i < negatives.length; i++) {
      negativesColors.push(chartColors.red);
    }
    const negativeDataset = {
      data: negatives,
      labels: 'Негативно',
      backgroundColor: negativesColors
    };

    this.answersChart = this.createOverallChart(
      labels,
      [
        positiveDataset,
        neutralDataset,
        negativeDataset
      ],
      [],
    );
  }

  buildTemperatureChart() {
    const data = [
      this.allProposals[this.currentProposal].sumPositive,
      this.allProposals[this.currentProposal].sumNegative,
      this.allProposals[this.currentProposal].sumNeutral,
    ];

    const labels = [
      'Позитивно',
      'Негативно',
      'Нейтрально'
    ];

    this.temperatureChart = this.createTemperatureChart(
      labels,
      data,
      [],
    );
  }

  private createAnswersChart(labels, data, barColors) {
    return new Chart(this.canvasElement.nativeElement, {
      type: 'horizontalBar',
      data: {
        labels: labels,
        datasets: [{
          data: data,
          backgroundColor: [
            chartColors.green,
            chartColors.blue,
            chartColors.purple,
            chartColors.red
          ]
        }]
      },
      options: {
        legend: {
          display: false
        },
        responsive: true,
        title: {
          display: true,
          text: 'Результаты опроса'
        },
        scales: {
          xAxes: [{
            ticks: {
              beginAtZero: true
            }
          }]
        }
      }
    });
  }

  private createOverallChart(labels, data, barColors) {
    return new Chart(this.overallElement.nativeElement, {
      type: 'horizontalBar',
      data: {
        labels: labels,
        datasets: data
      },
      options: {
        legend: {
          display: false
        },
        responsive: true,
        title: {
          display: true,
          text: 'Результаты опроса'
        },
        scales: {
          xAxes: [{
            ticks: {
              beginAtZero: true
            }
          }]
        }
      }
    });
  }

  private createTemperatureChart(labels, data, barColors) {
    return new Chart(this.temperatureElement.nativeElement, {
      type: 'doughnut',
      data: {
        labels: labels,
        datasets: [{
          label: 'Dataset 1',
          data: data,
          backgroundColor: [
            chartColors.red,
            chartColors.orange,
            chartColors.yellow,
            chartColors.green,
            chartColors.blue,
            chartColors.grey
          ]
        }]
      },
      options: {
        responsive: true,
        legend: {
          display: false
        },
        title: {
          display: true,
          text: 'Результат анализа комментариев'
        },
        animation: {
          animateScale: true,
          animateRotate: true
        }
      }
    });
  }
}
