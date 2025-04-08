import { Routes } from '@angular/router';
import {VacancyComponent} from './vacancy/vacancy.component';
import {AppComponent} from './app.component';

export const routes: Routes = [
  // {path: 'companies', component: AppComponent},
  {path: 'companies/:id/vacancies', component: VacancyComponent},
];
