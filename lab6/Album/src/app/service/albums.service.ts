import { Injectable } from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {Album} from '../albums/albums.component';
import {Photo} from '../albums/albums.component';
import {Observable} from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class AlbumsService {

  private url: string = "https://jsonplaceholder.typicode.com/albums";
  // private urlAlbumsLocal = "/assets/albums.json";
  // private urlPhotosLocal = "/assets/photos.json";
  constructor(private http: HttpClient) {
  }

  getAlbums(): Observable<Album[]> {
    return this.http.get<Album[]>(this.url);
    // return this.http.get<Album[]>(this.urlAlbumsLocal);
  }

  getAlbum(id: number): Observable<Album> {
    return this.http.get<Album>( this.url + `/${id}`) ;
    // return this.http.get<Album>(this.urlAlbumsLocal + `/${id}`);
  }
  getAlbumPhotos(id: number): Observable<Photo[]> {
    return this.http.get<Photo[]>( this.url + `/${id}/photos` ) ;
      // return this.http.get<Photo[]>( this.urlPhotosLocal ) ;
  }
}
