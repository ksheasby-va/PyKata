export class Pokemon {
  id: number;
  name: string;
  weight: number;
  height: number;
  types: string[];
  moves: Move[];
}

export class Move {
  name: string;
  methods: MoveMethod[];

  constructor(name: string, methods: MoveMethod[]) {
    this.name = name;
    this.methods = methods;
  }
}

export class MoveMethod {
  method: string;
  version: string;
  level: number;

  constructor(method: string, version: string, level: number) {
    this.method = method;
    this.version = version;
    this.level = level;
  }
}
