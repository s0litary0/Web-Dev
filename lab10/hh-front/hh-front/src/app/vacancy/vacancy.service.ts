import { Injectable } from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {Vacancy} from '../interfaces/vacancy';

@Injectable({
  providedIn: 'root'
})
export class VacancyService {

  baseUrl = 'http://127.0.0.1:8000';
  constructor(private http: HttpClient) {
  }

  getVacancies(id: number) {
    return this.http.get<Vacancy[]>(`${this.baseUrl}/api/companies/${id}/vacancies`);
  }
}
