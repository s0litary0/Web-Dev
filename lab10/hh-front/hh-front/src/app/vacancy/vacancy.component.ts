import {Component, OnInit} from '@angular/core';
import {Vacancy} from '../interfaces/vacancy';
import {ActivatedRoute} from '@angular/router';
import {VacancyService} from './vacancy.service';
import {CommonModule} from '@angular/common';

@Component({
  selector: 'app-vacancy',
  imports: [CommonModule],
  templateUrl: './vacancy.component.html',
  styleUrl: './vacancy.component.css'
})
export class VacancyComponent implements OnInit {
  vacancies: Vacancy[] = [];

  constructor(private route: ActivatedRoute, private vacancyService: VacancyService) {}

  ngOnInit() {
    let id = this.route.snapshot.paramMap.get('id');
    let companyId = Number(id)
    console.log(companyId);
      this.vacancyService.getVacancies(companyId).subscribe((vacancies: Vacancy[]) => {
        this.vacancies = vacancies;
        console.log(this.vacancies);
      });
  }
}

