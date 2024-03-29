# Metodyki CSS – BEM

- Części bloku łączyć znakiem "-" (np: .block-snake-tail).
- Element nie powinien mieć swojego elementu.

## Blok, element, modyfikator

```css
.block {
  /* code for the whole block */
}
.block--modifier {
  /* code for specific variant of the block */
}

.block-snake {
  /* code for the whole block */
}
.block-snake--modifier {
  /* code for specific variant of the block */
}

.block__element {
  /* code for element of the block */
}
.block__element--modifier {
  /* code for specific variant of the element */
}
```

## Zagnieżdżanie elementów

### Przykład 1

Prosty przykład bloku w bloku.

```html
<section class="section">
    <header class="header">
        <h1 class="header__title header__title--light">Title</h1>
    </header>

    <article class="section__article">
        <div class="article">
            <h2 class="article__title">Title goes here</h2>
            <div class="article__content">Text goes here</div>
        </div>
    </article>

    <div class="section__comments">
        <h2>Comments</h2>
        <div class="comment">
            <div class="comment__author"></div>
            <div class="comment__text"></div>
        </div>

        <div class="comment">
            <div class="comment__author"></div>
            <div class="comment__text"></div>
        </div>
    </div>
</section>
```

### Przykład 2

Blok umieszczony w bloku dla wielu komponentów (zamień słowo "box" na "box-25").

```html
<section class="box">
    <header class="box-header">
        <h1 class="box-header__title box-header__title--light">Title</h1>
    </header>

    <article class="box__article">
        <p class="">Text goes here</p>
    </article>

    <div class="box-comments">
        <h2 class="box-comments__title">Comments</h2>

        <div class="box-comment">
            <div class="box-comment__author"></div>
            <div class="box-comment__text"></div>
        </div>

        <div class="box-comment">
            <div class="box-comment__author"></div>
            <div class="box-comment__text"></div>
        </div>
    </div>
</section>
```

### Przykład 3

```css
.header {
  background: #fff;
}

.header__logo {
  margin-left: 50px;
  padding: 20px 0;
}

.header__logo--small {
    padding: 10px 0;
}

.logo {
  width: 100px;
  height: 100px;
  border: 1px solid #eee;
}

.logo--noborder {
    border: 1px solid transparent;
}

/*
<header class="header">
  <div class="header__logo logo header__logo--small logo--noborder"></div>
</header>
*/

.text {
  font-family: 'Open Sans';
  font-size: 14px;
}

/* <div class="article__content text"></div> */
```
