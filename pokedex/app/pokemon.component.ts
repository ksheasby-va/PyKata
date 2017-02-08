import { Component, OnInit, Input } from '@angular/core';

import { Pokemon } from './pokemon';
import { PokemonService } from './pokemon.service';

@Component({
  moduleId: module.id,
  selector: 'pokemon',
  templateUrl: 'pokemon.component.html',
})

export class PokemonComponent {
  @Input()
  pokemon: Pokemon;
  number: number;

  constructor(
    private pokemonService: PokemonService,
  ) { }

  lookupPokemon(): void {
    this.pokemonService.getPokemon(this.number)
      .then(pokemon => this.pokemon = pokemon);
  }
}
