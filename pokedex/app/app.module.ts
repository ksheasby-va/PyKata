import { NgModule }      from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpModule } from '@angular/http';
import { FormsModule } from '@angular/forms';

import { AppComponent }  from './app.component';
import { PokemonComponent } from './pokemon.component';
import { PokemonService } from './pokemon.service';

@NgModule({
  imports:      [ BrowserModule, HttpModule, FormsModule ],
  declarations: [ AppComponent, PokemonComponent ],
  providers: [ PokemonService ],
  bootstrap:    [ AppComponent ]
})
export class AppModule { }
