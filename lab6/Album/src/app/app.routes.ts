import { Routes } from '@angular/router';
import {HomeComponent} from './home/home.component';
import {AboutComponent} from './about/about.component';
import {AlbumsComponent} from './albums/albums.component';
import {AlbumDetailComponent} from './album-detail/album-detail.component';
import {PhotosComponent} from './photos/photos.component';

let AlbumDetailComponentComponent;
export const routes: Routes = [
  {path: '', redirectTo: '/home', pathMatch: 'full'},
  {path: 'home', component: HomeComponent, title: "Home"},
  {path: 'about', component: AboutComponent, title: "About"},
  {path: 'albums', component: AlbumsComponent, title: "Albums"},
  {path: 'albums/:id', component: AlbumDetailComponent, title: "Album detail"},
  {path: 'albums/:id/photos', component: PhotosComponent, title: "Photos"},
];
