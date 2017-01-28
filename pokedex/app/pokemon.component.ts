import { Component, OnInit, Input } from '@angular/core';

import { Pokemon } from './pokemon';
import { PokemonService } from './pokemon.service';

@Component({
  moduleId: module.id,
  selector: 'pokemon',
  templateUrl: 'pokemon.component.html',
})

export class PokemonComponent implements OnInit {
  @Input()
  pokemon: Pokemon;

  constructor(
    private pokemonService: PokemonService,
  ) { }

  ngOnInit(): void {
    this.pokemonService.getPokemon(19)
      .then(pokemon => this.pokemon = pokemon);
  }
}
