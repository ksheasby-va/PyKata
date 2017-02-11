import { Injectable } from '@angular/core';
import { Move, MoveMethod } from './pokemon';

@Injectable()
export class DataCleaningService {
  constructor() { }

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
