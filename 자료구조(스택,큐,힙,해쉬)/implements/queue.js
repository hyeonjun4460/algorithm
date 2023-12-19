class Node {
  constructor(data) {
    this.data = data;
    this.next = null;
  }
}

// 큐 클래스
class Queue {
  constructor() {
    this.head = null; // 제일 앞 노드
    this.rear = null; // 제일 뒤 노드
    this.length = 0; // 노드의 길이
  }

  enqueue(data) { // 노드 추가.
    const node = new Node(data); // data를 가진 node를 만들어준다.
    if (!this.head) { // 헤드가 없을 경우 head를 해당 노드로
      this.head = node;
    } else {
      this.rear.next = node; // 아닐 경우 마지막의 다음 노드로
    }
    this.rear = node; // 마지막을 해당 노드로 한다.
    this.length++;
  }

  dequeue() { // 노드 삭제.
    if (!this.head) { // 헤드가 없으면 한 개도 없는 것이므로 false를 반환.
      return false;
    }
    const data = this.head.data; // head를 head의 다음 것으로 바꿔주고 뺀 data를 return
    this.head = this.head.next;
    this.length--;

    return data;
  }
}

const queue = new Queue()
queue.enqueue(1)
console.log(queue)
queue.enqueue(2)
console.log(queue)
queue.enqueue(3)
console.log(queue)
queue.enqueue(4)
console.log(queue)

console.log(queue.dequeue()) //1
console.log(queue.dequeue()) //2
console.log(queue.dequeue()) //3
console.log(queue.dequeue()) //4

// 객체는 힙메모리에 저장되고, 변수나 이를 사용하는 함수, 객체에서는 이에 대한 참조만을 사용함.
// 참조하는 함수에서 이에 대한 변경은 곧, 힙메모리에 저장된 객체를 변경하는 것임.
// 그래서 this.head.next가 계속 next로 꼬리를 무는 것임.
// 얕은 복사는 다음 예시에서 obj2를 변경하는 경우를 얕은 복사의 경우임.(원본까지 변경하는 변수 할당)

// //let obj1 = { key: "value" };
// let obj2 = obj1; // obj1의 참조가 obj2에 복사됨

// console.log(obj1); // { key: "value" }
// console.log(obj2); // { key: "value" }

// obj1.key = "updatedValue";
// console.log(obj1); // { key: "updatedValue" }
// console.log(obj2); // { key: "updatedValue" }