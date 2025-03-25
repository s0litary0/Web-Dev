import {Injectable} from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {Observable} from 'rxjs';
import {Category} from '../enums/Category';
import {Product} from '../interfaces/Product';

@Injectable({
  providedIn: 'root'
})
export class ProductListService {

  constructor(private http: HttpClient) { }

  getCategory(category: string | null): Observable<Product[]> {
    if (category === Category.PHONES) {
      return this.http.get<Product[]>("http://localhost:3000/phones");
    }
    else if (category === Category.LAPTOPS) {
      return this.http.get<Product[]>("http://localhost:3000/laptops");
    }
    else if (category === Category.SHOES) {
      return this.http.get<Product[]>("http://localhost:3000/shoes");
    }
    else {
      return this.http.get<Product[]>("http://localhost:3000/books");
    }
  }
}
