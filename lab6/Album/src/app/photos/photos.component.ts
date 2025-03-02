import {Component, OnInit} from '@angular/core';
import {CommonModule} from '@angular/common';
import {AlbumsService} from '../service/albums.service';
import {ActivatedRoute, RouterLink} from '@angular/router';
import {Photo} from '../albums/albums.component';

@Component({
  selector: 'app-photos',
  imports: [
    CommonModule,
    RouterLink,
  ],
  templateUrl: './photos.component.html',
  styleUrl: './photos.component.css'
})
export class PhotosComponent implements OnInit {
  photos!: Photo[];
  loaded: boolean = false;

  constructor(private route: ActivatedRoute, private albumService: AlbumsService) {
  }

  ngOnInit(): void {
    this.route.paramMap.subscribe( params => {
      const id = Number(params.get('id'));
        // this.album = this.albumService.getAlbums().subscribe(albums)
      this.albumService.getAlbumPhotos(id).subscribe((photos) => {
        this.photos = photos;
        console.log(this.photos);
        this.loaded = true;
      })
    })
  }

}
