import React from 'react';
import type {Meta, StoryObj} from '@storybook/react';

import {Name_Adder} from './Name_Adder';

const meta: Meta<typeof Name_Adder> = {
  component: Name_Adder,
};

export default meta;

type Story = StoryObj<typeof Name_Adder>;

export const Basic: Story = {args: {}};
