from typing import List, Optional
from pydantic import BaseModel

class Comment(BaseModel) :
    id : int
    content : str
    replies : Optional[List['Comment']] = None

Comment.model_rebuild()
# required after self reference classes beacause performance degrades

comment = Comment(
    id = 1,
    content = "First Comment",
    replies = [
        Comment(id = 2, content = "Reply 1"),
        Comment(id = 3, content = "Reply 2", replies = [
            Comment(id = 4, content = "Nested reply")
        ]),
    ],
)

print(f"Comment  : {comment}")