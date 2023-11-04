import * as React from 'react';
import {
  Box,
  Center,
  Input,
  Text,
  FormControl,
  FormLabel,
  theme,
} from '@chakra-ui/react';
import { Button } from '@chakra-ui/react';
import { Link } from '@chakra-ui/react';

import { ChakraProvider } from '@chakra-ui/react';

const headStyle = {
  textAlign: 'center',
  aligItems: 'center',
  justifyContent: 'center',
  margin: '20px 60px 30px 60px',
};

const btnStyle = {
  display: 'flex',
  aligItems: 'center',
  justifyContent: 'center',
  margin: '20px 60px 0 60px',
};

export default function Login() {
  return (
    <ChakraProvider theme={theme}>
      <Center>
        <Box p="10" maxW="620px" borderWidth="2px">
          <Text
            mt={2}
            fontSize="xl"
            fontWeight="bold"
            lineHeight="short"
            style={headStyle}
          >
            LOGIN in to
          </Text>
          <FormControl>
            <FormLabel htmlFor="email">Email address</FormLabel>
            <Input id="email" type="email" />

            <FormLabel htmlFor="password">Password</FormLabel>
            <Input id="password" type="password" />
          </FormControl>
          <Button colorScheme="blue" variant="ghost" style={btnStyle}>
            Submit
          </Button>
          <Link color="blue.500" href="#">
            Don't have an Account ?
          </Link>
          <Button colorScheme="blue" variant="solid" style={btnStyle}>
            Sign Up
          </Button>
        </Box>
      </Center>
    </ChakraProvider>
  );
}
