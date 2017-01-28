import { Injectable } from '@angular/core';
import { Headers, Http } from '@angular/http';

import 'rxjs/add/operator/toPromise';

import { Pokemon } from './pokemon';

@Injectable()
export class PokemonService {
  private headers = new Headers({'Accept': 'application/json'});
  private pokemonUrl = 'http://pokeapi.co/api/v2/pokemon';

  constructor(private http: Http) { }

  getPokemon(number: number): Promise<Pokemon> {
    const url = `${this.pokemonUrl}/${number}/`;
    return this.http.get(url, this.headers)
      .toPromise()
      .then(response => response.json() as Pokemon)
  }
}
