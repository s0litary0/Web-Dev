import {Component, OnInit} from '@angular/core';
import {ActivatedRoute, RouterLink} from '@angular/router';
import {Album} from '../albums/albums.component';
import {AlbumsService} from '../service/albums.service';
import {CommonModule} from '@angular/common';
import {FormsModule} from '@angular/forms';

interface Editable {
  changeTitle(title: string): void;
}

@Component({
  selector: 'app-album-detail',
  imports: [CommonModule, FormsModule, RouterLink],
  templateUrl: './album-detail.component.html',
  styleUrl: './album-detail.component.css'
})
export class AlbumDetailComponent implements OnInit, Editable {
  album!: Album;
  loaded: boolean = false;
  newTitle: string ="";
  constructor( private route: ActivatedRoute, private albumService: AlbumsService ) {
  }

  ngOnInit(): void {
    this.route.paramMap.subscribe( params => {
      const id = Number(params.get('id'));
    //   this.album = this.albumService.getAlbums().subscribe(albums)
    this.albumService.getAlbum(id).subscribe((album) => {
      this.album = album;
      this.loaded = true;
    })
    })
  }

  changeTitle(title: string): void {
    this.album.title = title;
  }
}
