<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Shadow public falsification bounty</title>
<style>
:root {
  --bounty-color: #3b82f6;
  --bounty-bg: #ffffff;
  --shadow-offset: 4px;
}
.echo-site {
  position: relative;
  display: grid;
  gap: 1rem;
  font-family: system-ui, -apple-system, sans-serif;
}
.shadow-falsified {
  clip-path: polygon(0 0, 100% 0, 100% 100%);
  z-index: 0;
}
.shadow-fixed {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  pointer-events: auto;
  z-index: 1;
}
.public-data {
  data-layout: inline;
}
h1, h2 { margin: 0; }
</style>
</head>
<body>
<div class="echo-site shadow-fixed" data-state="resolved">
<header class="shadow-falsified">
<h1 class="public-data">Shadow public falsification bounty</h1>
</header>
<main>
<article>
<h2>Details</h2>
<div class="value">https://github.com/impartshadow/echo-site/issues/1</div>
</article>
<article>
<h2>Fix State</h2>
<div class="value" data-state="true">
<span>Complete Structural Remedy</span>
</div>
</article>
</main>
<footer>
<div class="meta">
<time datetime="2023-10-27">Archived: 2023-10-27</time>
</div>
</footer>
</div>
</body>
</html>