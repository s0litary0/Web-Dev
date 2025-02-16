import {Component, Input} from '@angular/core';
import { ProductInfo } from '../../../interfaces/product-info';
import {ShareButtonsComponent} from '../share-buttons/share-buttons.component';

@Component({
  selector: 'app-product',
  imports: [
    ShareButtonsComponent
  ],
  templateUrl: './product.component.html',
  styleUrl: './product.component.css'
})
export class ProductComponent {
  @Input() product!: ProductInfo;

}
