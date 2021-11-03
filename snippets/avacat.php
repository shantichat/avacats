function avacat ($name, $size, $num = 255) {
  $i = crc32(mb_strtolower($name)) % $num;
  return "https://shantichat.github.io/avacats/$sizex$size/$i.jpg";
}

echo avacat ('alice@example.com', 80);
// https://shantichat.github.io/avacats/80/171.jpg

echo avacat ('bob@example.com', 120);
// https://shantichat.github.io/avacats/120/222.jpg
