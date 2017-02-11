import 'rxjs/add/operator/switchMap'
import { Component, OnInit, Input } from '@angular/core';
import { ActivatedRoute, Params } from '@angular/router';

import { Pokemon, Move, MoveMethod } from './pokemon';
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
      .subscribe(function(pokemon: Pokemon) {
        this.pokemon = pokemon;
        this.pokemon.types = this.getTypes(pokemon);
        this.pokemon.moves = this.getMoves(pokemon);
      }.bind(this));
  }

  getTypes(pokemon: any): string[] {
    let types: string[] = [];
    for (let type of pokemon.types) {
      types.push(type.type.name);
    }
    return types;
  }

  getMoves(pokemon: any): Move[] {
    let moves: Move[] = [];
    for (let move of pokemon.moves) {
      let moveMethods = this.getMoveMethods(move);
      if (moveMethods.length > 0) {
        moves.push(new Move(move.move.name, moveMethods));
      }
    }
    return moves;
  }

  getMoveMethods(move: any): MoveMethod[] {
    let moveMethods: MoveMethod[] = [];
    for (let method of move.version_group_details) {
      if (method.move_learn_method.name === 'level-up') {
        moveMethods.push(new MoveMethod(method.move_learn_method.name, method.version_group.name,
          method.level_learned_at));
      }
    }
    return moveMethods;
  }
}
