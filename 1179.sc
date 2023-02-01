import java.time.Instant

def debounce[Input, Output](f: (Input) => Output, n: Int): Input => Option[Output] = {
  var lastCalledAt: Long = 0
  (input: Input) => {
    val now = Instant.now().getEpochSecond * 1000
    if ((lastCalledAt + n) < now) {
      lastCalledAt = now
      Some(f(input))
    } else None
  }
}

val myFn = (num: Int) => println(s"hello $num!")
val myDebouncedFn = debounce(myFn, 100)
(0 to 399999999).map(myDebouncedFn)
