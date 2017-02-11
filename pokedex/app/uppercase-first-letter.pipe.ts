import {Pipe, PipeTransform} from '@angular/core';

@Pipe({name: 'uppercaseFirstLetters'})
export class UppercaseFirstLettersPipe implements PipeTransform {
  transform(words: string): string {
    let wordsArray = words.split(/ |-/);

    let uppercaseArray: string[] = [];
    for (let singleWord of wordsArray) {
      let uppercaseWord = singleWord.charAt(0).toUpperCase() + singleWord.slice(1);
      uppercaseArray.push(uppercaseWord);
    }

    return uppercaseArray.join(' ');
  }
}
