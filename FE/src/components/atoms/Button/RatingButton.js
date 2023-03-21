import React from "react";
import { RatingBtn } from "../../../styles/common/ButtonsStyle";

function RatingButton({ isSelected, height }) {
	return (
		<RatingBtn
			viewBox="0 0 22 21"
			fill="none"
			xmlns="http://www.w3.org/2000/svg"
			isSelected={isSelected}
			height={height}
		>
			<path d="M10.6315 16.1699L17.1368 20.0962L15.4105 12.6962L21.1579 7.71724L13.5894 7.07514L10.6315 0.0961914L7.67365 7.07514L0.105225 7.71724L5.85259 12.6962L4.12628 20.0962L10.6315 16.1699Z" />
		</RatingBtn>
	);
}

export default RatingButton;
