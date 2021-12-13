#include<iostream>
#include<string>
#define MAX 100
using namespace std;
template <typename T>
class Queue
{
	
	int front;
	int rare;
	T queue[MAX];
	public:
	Queue()
	{
		front = 0;
		rare = -1;
	}
	
	bool isFull();
	bool isEmpty();
	void push(T data);
	void dIQueue();
	int cPFront();
	int cPRare();
	T cREle();
	
};

template <typename T>
T Queue<T>::cREle()
{
	return queue[front];
}

template <typename T>
int Queue<T>::cPFront()
{
	return front;
}

template <typename T>
int Queue<T>::cPRare()
{
	return rare;
}

template <typename T>
void Queue<T>::push(T data)
{
	if(isFull())
	{
		cout<<"Queue is Full";
		
	}
	else
	{
		rare++;
		queue[rare] = data;
	}
}

template <typename T>
void Queue<T>::dIQueue()
{
	if(isEmpty())
	{
		cout<<"Queue is empty";
	}
	else
	{
		if(front!=MAX)
			front++;	
		else
			front = 0;
	}
}

template <typename T>
bool Queue<T>::isEmpty()
{
	if (front==MAX ||  rare == -1)
	{
		return true;
	}
	else{
		return false;
	}
}

template <typename T>
bool Queue<T>::isFull()
{
	if (rare>=MAX-1)
	{
		return true;
	}
	else
	{
		return false;
	}
}

int main()
{
	Queue<int> q1;
	q1.dIQueue();
	cout<<endl;
	int n;
	int num;
	cout<<"Total process count: ";
	cin>>n;
	for(int i=0; i<n; i++)
	{
		cout<<"Enter process id: ";
		cin>>num;
		q1.push(num);
	}
	cout<<"Process execution as per FIFO: ";
	for(int i=0; i<=q1.cPRare(); i++)
	{
		cout<<q1.cREle()<<" ";
		q1.dIQueue();
	}
	return 0;
}
