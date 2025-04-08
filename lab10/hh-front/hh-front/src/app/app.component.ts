import {Component, OnInit} from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { CommonModule } from '@angular/common';
import {CompanyComponent} from './company/company.component';
import {Company} from './interfaces/company';
import {CompanyService} from './company/company.service';


@Component({
  selector: 'app-root',
  imports: [CommonModule, CompanyComponent, RouterOutlet],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent implements OnInit {
  title = 'hh-front';

  companies: Company[] = []

  constructor(private companyService: CompanyService) { }

  ngOnInit(): void {
    this.companyService.getCompanies().subscribe(
        (companies: Company[]) => {
          this.companies = companies;
          console.log(this.companies);
        }
    )
  }

}
