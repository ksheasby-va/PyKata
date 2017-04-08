import { Component, Input, OnInit, ViewChild } from '@angular/core';
import { PokemonService } from './pokemon.service';
import { ActivatedRoute, Params } from '@angular/router';
import { Pokemon } from './pokemon';
import { DataCleaningService } from './data-cleaning.service';
import { ModalComponent } from 'ng2-bs3-modal/components/modal';

@Component({
  moduleId: module.id,
  selector: 'move-details',
  templateUrl: 'move-details.component.html',
})

export class MoveDetailComponent implements OnInit {
  @Input()
  pokemon: Pokemon;

  @ViewChild('modal')
  modal: ModalComponent;
  // items: string[] = [];


  constructor(private pokemonService: PokemonService,
              private dataCleaningService: DataCleaningService,
              private route: ActivatedRoute,) { }

  ngOnInit(): void {
    this.route.params
      .switchMap((params: Params) =>
        this.pokemonService.getPokemon(+params[ 'id' ]))
      .subscribe(function (pokemon: Pokemon) {
        this.pokemon = pokemon;
        this.pokemon.moves = this.dataCleaningService.getMoves(pokemon);
      }.bind(this));
  }

  open() {
    this.modal.open();
  }
}
