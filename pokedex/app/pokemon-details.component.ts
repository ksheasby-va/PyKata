import 'rxjs/add/operator/switchMap'
import { Component, OnInit, Input } from '@angular/core';
import { ActivatedRoute, Params } from '@angular/router';

import { Pokemon } from './pokemon';
import { PokemonService } from './pokemon.service';

@Component({
  moduleId: module.id,
  selector: 'pokemon-details',
  templateUrl: 'pokemon-details.component.html',
})

export class PokemonDetailComponent implements OnInit {
  @Input()
  pokemon: Pokemon;

  constructor(
    private pokemonService: PokemonService,
    private route: ActivatedRoute,
  ) { }

  ngOnInit(): void {
    this.route.params
      .switchMap((params: Params) =>
        this.pokemonService.getPokemon(+params['id']))
      .subscribe(pokemon => this.pokemon = pokemon);
  }
}
