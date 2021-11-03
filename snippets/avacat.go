package main

import (
	"fmt"
	"strings"
	"hash/crc32"
)

func main() {
	fmt.Println(Avacat("alice@example.com", 80)) // https://shantichat.github.io/avacats/80x80/171.jpg
	fmt.Println(Avacat("bob@example.com", 120))  // https://shantichat.github.io/avacats/120x120/222.jpg
}

func Avacat(name string, size int) string {
	const maxNum = 255
	i := crc32.ChecksumIEEE([]byte(strings.ToLower(name))) % maxNum
	return fmt.Sprintf("https://shantichat.github.io/avacats/%dx%d/%d.jpg", size, size, i)
}
