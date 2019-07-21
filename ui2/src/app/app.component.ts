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
      });
  }

  selectProposal(id) {
    let index = 0;
    this.allProposals.find((el, i)=> {
      if (el.id === id){
        index = i;
        return true;
      }
      return false;
    });

    this.currentProposal = index;
    setTimeout(() => {
      console.log('Waiting for the element');
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
    }, 1000);

  }

  eraseSelection() {
    this.currentProposal = null;
  }

  private createAnswersChart(labels, data, barColors) {
    return new Chart(this.canvasElement.nativeElement, {
      type: 'horizontalBar',
      data: {
        labels: labels,
        datasets: [{
          data: [25,50,26,0],
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
}
