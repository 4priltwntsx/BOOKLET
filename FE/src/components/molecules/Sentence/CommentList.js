import React from "react";
import { Container } from "../../../styles/common/ContainingsStyle";
import Comment from "../Comment";

function CommentList({ comments, type, getCommentApiCall }) {
	return (
		<Container marginTop="16">
			{comments?.map((comment) => (
				<Comment
					key={comment.cId}
					comment={comment}
					type={type}
					getCommentApiCall={getCommentApiCall}
				/>
			))}
		</Container>
	);
}

export default CommentList;
