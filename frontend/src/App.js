import Wrapper from "./components/Wrapper";
import Screen from "./components/Screen";
import ButtonBox from "./components/ButtonBox";
import Button from "./components/Button";

const btnValues = [
  ["CSV", "AC", "+-", "/"],
  [7, 8, 9, "*"],
  [4, 5, 6, "-"],
  [1, 2, 3, "+"],
  [0, ".", "="],
];

const App = () => {
  return (
   <Wrapper>
    <Screen value="0" />
    <ButtonBox>
      {
        btnValues.flat().map((btn, i) => {
          return (
            <Button
              key={i}
              className={(btn == "=" ? "equals" : "") || (btn == "AC" ? "clear" : "") || (btn == "CSV" ? "export" : "")} 
              value={btn}
              onClick={() => {
                console.log("Button clicked!");
              }}
            />
          );
        })  
      }
    </ButtonBox>
   </Wrapper>
  );
}

export default App;
