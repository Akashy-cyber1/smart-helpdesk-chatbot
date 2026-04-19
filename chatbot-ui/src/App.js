import React, { useState, useEffect, useRef } from "react";

// const API_URL = process.env.REACT_APP_API_URL;
const API_URL = process.env.REACT_APP_API_URL || "http://localhost:8000";

export default function ChatbotUI() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);
  const chatEndRef = useRef(null);

  const sendMessage = async () => {
    if (!input.trim()) return;

    const userMessage = { sender: "user", text: input };
    setMessages((prev) => [...prev, userMessage]);
    setLoading(true);

    try {
      const res = await fetch(`${API_URL}/chat`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ message: input }),
      });

      if (!res.ok) throw new Error("Server error");

      const data = await res.json();

      const botMessage = {
        sender: "bot",
        text: data.response || "No response",
      };

      setMessages((prev) => [...prev, botMessage]);
    } catch (error) {
      const errorMessage = {
        sender: "bot",
        text: "⚠️ Cannot connect to backend",
      };
      setMessages((prev) => [...prev, errorMessage]);
    }

    setInput("");
    setLoading(false);
  };

  useEffect(() => {
    chatEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages]);

  return (
    <div className="h-screen flex bg-gray-200">
      {/* Sidebar */}
      {/* <div className="w-1/4 bg-white border-r hidden md:block">
        <div className="p-4 font-bold text-lg border-b">Chats</div>
        <div className="p-3 hover:bg-gray-100 cursor-pointer">AI Chatbot</div>
      </div> */}

      {/* Chat Area */}
      <div className="flex-1 flex flex-col">
        {/* Header */}
        <div className="bg-green-600 text-white p-4 font-semibold shadow">
          AI Chatbot
        </div>

        {/* Messages */}
        <div className="flex-1 overflow-y-auto p-4 space-y-2 bg-[url('https://www.transparenttextures.com/patterns/cubes.png')]">
          {messages.map((msg, index) => (
            <div
              key={index}
              className={`flex ${
                msg.sender === "user" ? "justify-end" : "justify-start"
              }`}
            >
              <div
                className={`px-4 py-2 rounded-2xl max-w-xs shadow ${
                  msg.sender === "user"
                    ? "bg-green-500 text-white"
                    : "bg-white"
                }`}
              >
                {msg.text}
              </div>
            </div>
          ))}

          {loading && (
            <div className="text-sm text-gray-500">Typing...</div>
          )}

          <div ref={chatEndRef} />
        </div>

        {/* Input */}
        <div className="p-3 bg-white flex items-center gap-2 border-t">
          <input
            type="text"
            value={input}
            onChange={(e) => setInput(e.target.value)}
            placeholder="Type a message"
            className="flex-1 border rounded-full px-4 py-2 outline-none"
            onKeyDown={(e) => e.key === "Enter" && sendMessage()}
          />

          <button
            onClick={sendMessage}
            className="bg-green-500 text-white px-4 py-2 rounded-full"
          >
            ➤
          </button>
        </div>
      </div>
    </div>
  );
}
