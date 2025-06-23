from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from app.services.logs_service import answer_log_question

router = APIRouter()

@router.websocket("/ws/chat")
async def websocket_log_chat(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            # receive question from client
            user_question = await websocket.receive_text()

            # Process the question using our log-based LLM fn
            answer = await answer_log_question(user_question)

            # send the answer back to the web socket
            await websocket.send_text(answer)
    except WebSocketDisconnect:
        print("client disconnected from WebSocket")
