def swapEveryTwoNodes[A](linkedList: List[A]): List[A] = linkedList match {
  case Nil => Nil
  case x :: Nil => x :: Nil
  case x1 :: x2 :: xs => x2 :: x1 :: swapEveryTwoNodes(xs)
}

println(swapEveryTwoNodes(List(1, 2, 3, 4)))