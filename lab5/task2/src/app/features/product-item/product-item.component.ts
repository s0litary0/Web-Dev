import {Component, Input, OnInit} from '@angular/core';
import {Product} from '../interfaces/Product';
import {ProductItemService} from './product-item.service';


@Component({
  selector: 'product-item',
  imports: [],
  templateUrl: './product-item.component.html',
  styleUrl: './product-item.component.css'
})
export class ProductItemComponent implements OnInit {
  @Input() product!: Product;
  @Input() category!: string | null | undefined;
  constructor(private productItemService: ProductItemService) {

  }

  ngOnInit() { console.log(this.product); }

  updateLikes() {
    let updatedLikes: object = {likes: this.product.likes + 1};
    this.productItemService.updateLikes(this.category, this.product.id, updatedLikes).subscribe(
      response => {
        console.log('Product field updated:', response);
        this.product.likes = response.likes;
      }
    );
  }

}
