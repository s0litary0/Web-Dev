import {Component, Input} from '@angular/core';
import {ProductInfo} from '../../../interfaces/product-info';

@Component({
  selector: 'app-share-buttons',
  imports: [],
  templateUrl: './share-buttons.component.html',
  styleUrl: './share-buttons.component.css'
})
export class ShareButtonsComponent {
  @Input() product!: ProductInfo;

  shareOnTelegram() {
    let url: string = encodeURIComponent(this.product.href);
    window.open(`https://t.me/share/url?url=${url}&text=`, '_blank');
    console.log(this.product)
  }

  shareOnWhatsApp() {
    let url: string = encodeURIComponent(this.product.href);
    window.open(`https://api.whatsapp.com/send?text=%20${url}`, '_blank');
  }
}
