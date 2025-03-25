import {Component, OnInit} from '@angular/core';
import {ActivatedRoute, ParamMap} from '@angular/router';
import {Product} from '../interfaces/Product';
import {ProductListService} from './product-list.service';
import {Category} from '../enums/Category';
import {CommonModule} from '@angular/common';
import {preserveWhitespacesDefault} from '@angular/compiler';
import {ProductItemComponent} from '../product-item/product-item.component';

@Component({
  selector: 'product-list',
  imports: [CommonModule, ProductItemComponent,],
  templateUrl: './product-list.component.html',
  styleUrl: './product-list.component.css'
})
export class ProductListComponent implements OnInit {

  products?: Product[];
  category?: string | null | undefined = null;
  isLoaded = false;

  constructor(private productListService: ProductListService, private route: ActivatedRoute) {
  }

  ngOnInit() {

    this.route.paramMap.subscribe(
      (params: ParamMap): void => {
        console.log(params.get("category"));
        let requiredCategory: string | null = params.get("category");
        this.category = requiredCategory;

        this.productListService.getCategory(requiredCategory).subscribe(
          ( products: Product[] ): void => {
            this.products = products;
            this.isLoaded = true;
          }
        );
      }
    )
  }

  protected readonly preserveWhitespacesDefault = preserveWhitespacesDefault;
}
