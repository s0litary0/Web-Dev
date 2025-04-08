import { Injectable } from '@angular/core';
import { Company } from '../interfaces/company';
import {HttpClient} from '@angular/common/http';
import {Observable} from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class CompanyService {

  baseUrl: string = 'http://127.0.0.1:8000/';

  constructor(private http: HttpClient) {
  }

  getCompanies(): Observable<Company[]> {
    return this.http.get<Company[]>(`${this.baseUrl}api/companies/`);
  }

}
