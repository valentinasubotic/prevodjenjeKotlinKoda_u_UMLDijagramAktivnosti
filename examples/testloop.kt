fun testLoops() {
    var i: Int = 1
    while (i <= 5) {
        println(i)
        i = i + 1
    }

    var x: Int = 0
    while (x < 3) {
        x = x + 1
    }

    var y: Int = 0
    do {
        y++
    } while (y < 2)
}
