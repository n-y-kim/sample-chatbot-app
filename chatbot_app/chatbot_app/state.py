import reflex as rx
import asyncio

class State(rx.State):
    """The app state."""

    # The current question being asked
    question: str
    
    # Keep track of the chat history as a list of (question, answer) pairs
    chat_history: list[tuple[str, str]]
    
    async def answer(self):
        # if len(self.chat_history) == 0:
        #     self.greeting_message()
        """Return the answer to the current question."""
        answer = "I don't know yet. Sorry! I will connect to Azure OpenAI and get back to you."
        self.chat_history.append((self.question, answer))
        #Add streaming effect to the answer
        for i in range(len(answer)):
            #Pause to show the streaming effect.
            await asyncio.sleep(0.05)
            #Add one letter at a time to the output
            self.chat_history[-1] = (self.question, answer[:i+1])
            yield
            
    # async def greeting_message(self):
    #     answer = "Hello, I'm chatbot app to help you with your questions about Azure."
    #     self.chat_history.append(("", answer))
    #     self.streaming_effect(answer)

    