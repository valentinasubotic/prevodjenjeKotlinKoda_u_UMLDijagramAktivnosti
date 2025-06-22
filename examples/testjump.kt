fun test(x: Int) {
    when (x) {
        1 -> throw Exception("Greška")
        2 -> return
        else -> return
    }

    while (true) {
        if (x > 5) {
            break
        } else {
            continue
        }
    }
}
