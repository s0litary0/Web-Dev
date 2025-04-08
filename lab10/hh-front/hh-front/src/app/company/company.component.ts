import {Component, Input} from '@angular/core';
import {Company} from '../interfaces/company';
import {RouterLink, RouterOutlet} from '@angular/router';

@Component({
  selector: 'app-company',
  imports: [
    RouterLink,
    RouterOutlet
  ],
  templateUrl: './company.component.html',
  styleUrl: './company.component.css'
})
export class CompanyComponent {
  @Input() company!: Company;

}
