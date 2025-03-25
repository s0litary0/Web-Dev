import { Routes } from '@angular/router';

import { AppComponent } from './app.component';
import { ProductItemComponent} from './features/product-item/product-item.component';
import { ProductListComponent } from './features/product-list/product-list.component';


export const routes: Routes = [
  { path: 'products-list/:category', component: ProductListComponent },
];
