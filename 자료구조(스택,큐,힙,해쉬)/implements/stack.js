class Box {
  value;
  next;

  constructor(value) {
    this.value = value;
  }

  setPointer(box) {
    this.next = box;
  }
}

class Stack {
    node;

  push(value) {
    // 박스를 만든다.
    const newBox = new Box(value);

    // node가 없으면 바로 넣는다.
    if (!this.node) {
      this.node = newBox;
    } else {
        // node가 있다면, 새 박스의 next pointer는 현재 노드로 한다.
      newBox.setPointer(this.node);
      // node에 새 박스를 넣는다.
      this.node = newBox
    }
  }

  pop() {
    // 노드가 있으면 value를 리턴한다.
    if(this.node){
    const value = this.node.value;


// 노드에 다음 포인터가 있으면 현재 노드는 포인터의 노드로 바꾸고, 그렇지 않으면 노드를 삭제한다.
    if (this.node.next) {
      this.node = this.node.next;
    } else {
        delete this.node
    }

    return value;
    } else {
        return 'empty'
    }
  }
}

const stack = new Stack();
stack.push(1);
stack.push(2);
stack.push(3);

console.log(stack.pop()); // 3
console.log(stack.pop()); // 2
console.log(stack.pop()); // 1
console.log(stack.pop()); // empty
