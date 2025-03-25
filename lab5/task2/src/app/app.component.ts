import {Component} from '@angular/core';
import {RouterLink, RouterLinkActive, RouterOutlet} from '@angular/router';
import {CommonModule} from '@angular/common';
import {Category} from './features/enums/Category';

import {ProductListService} from './features/product-list/product-list.service';

@Component({
  selector: 'app-root',
  imports: [ CommonModule, RouterLink, RouterLinkActive, RouterOutlet ],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {

  constructor(private productListService: ProductListService) {

  }
  selectedCategory?: Category;



  categories?: Category[] = [
    Category.PHONES, Category.LAPTOPS, Category.SHOES, Category.BOOKS
  ];

}
