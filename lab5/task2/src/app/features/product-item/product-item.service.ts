import { Injectable } from '@angular/core';
import {Category} from '../enums/Category';
import {HttpClient} from '@angular/common/http';
import {Product} from '../interfaces/Product';
import {Observable} from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ProductItemService {

  constructor(private http: HttpClient) { }

  updateLikes(category: string | null | undefined, productId: number, updatedLikes: object): Observable<Product> {
    return this.http.patch<Product>(`http://localhost:3000/${category}/${productId}`, updatedLikes)
  }

}
