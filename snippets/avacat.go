package main

import (
	"fmt"
	"hash/crc32"
)

func main() {
	fmt.Println(Avacat("alice@example.com", 80)) // https://shantichat.github.io/avacats80x80/171.jpg
	fmt.Println(Avacat("bob@example.com", 120))  // https://shantichat.github.io/avacats120x120/222.jpg
}

func Avacat(name string, size int) string {
	const root = "https://shantichat.github.io/avacats"
	const maxNum = 255
	i := crc32.ChecksumIEEE([]byte(name)) % maxNum
	return fmt.Sprintf("%s/%dx%d/%d.jpg", root, size, size, i)
}
