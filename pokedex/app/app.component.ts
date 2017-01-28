import { Component } from '@angular/core';

@Component({
  selector: 'my-app',
  template: `<h1>{{name}}</h1>
  <pokemon></pokemon>
`,
})
export class AppComponent  { name = 'Angular Pokedex'; }
