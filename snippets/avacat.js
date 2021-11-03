function crc32 (str) {
  const crcTable = [];
  let c

  for (let i = 0; i < 256; i++) {
      c = i
      for (let j = 0; j < 8; j++){
          c = ((c & 1) ? (0xEDB88320 ^ (c >>> 1)) : (c >>> 1))
      }
      crcTable[i] = c;
  }

  let crc = 0 ^ (-1);

  for (let i = 0; i < str.length; i++) {
      crc = (crc >>> 8) ^ crcTable[(crc ^ str.charCodeAt(i)) & 0xFF]
  }

  return (crc ^ (-1)) >>> 0
}

function avacat (name, size, num = 255) {
  const i = crc32(name) % num
  return `https://shantichat.github.io/avacats/${size}x${size}/${i}.jpg`
}

console.log(avacat('alice@example.com', 80))
// https://shantichat.github.io/avacats/80/171.jpg

console.log(avacat('bob@example.com', 120))
// https://shantichat.github.io/avacats/120/222.jpg
