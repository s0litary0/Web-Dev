import {Component, OnInit} from '@angular/core';
import { CommonModule } from '@angular/common';
import {AlbumsService} from '../service/albums.service';
import {RouterLink} from '@angular/router';
import {FormsModule} from '@angular/forms';

export interface Album {
  userId: number;
  id: number;
  title: string;
}
export interface Photo {
  albumId: number;
  id: 1,
  title: string;
  url: string;
  thumbnailUrl: string;
}

interface CRUD {
  createAlbum(userId: number, id: number, title: string): Album;
  updateAlbum(album: Album): void;
  deleteAlbum(id: number): void;
}

@Component({
  selector: 'app-albums',
  imports: [CommonModule, RouterLink, FormsModule],
  templateUrl: './albums.component.html',
  styleUrl: './albums.component.css'
})
export class AlbumsComponent implements OnInit, CRUD {
  public albums!: Album[];
  newID!: number;
  newUserID!: number;
  newName!: string;
  constructor(private albumsService: AlbumsService) {
  }

  ngOnInit(): void {
    this.albumsService.getAlbums().subscribe((albums) => {this.albums = albums;});
    // console.log(this.albums);
    // console.log(1);
  }

  createAlbum(userId: number, id: number, title: string): Album {
    const album: Album = {
      userId, id, title
    }
    this.albums.push(album);
    return album;
  }

  deleteAlbum(id: number): void {
    const index = this.albums.findIndex((album) => album.id === id);
    if (index != -1) {
      this.albums.splice( index, 1 )
    }
  }

  updateAlbum(album: Album): void {
    return undefined;
  }
}
